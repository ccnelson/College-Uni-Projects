// C NELSON UoH 2020
// Action script implementing GoapAction abstract class
// Adapted from original script by
// Brent Owens (github.com/sploreg/goap)

using System.Linq;
using UnityEngine;

public class ChopTreeAction : GoapAction
{
	private ToolComponent tool = null;
	private TreeComponent[] trees = null;
	private TreeComponent closest = null;
	private IOrderedEnumerable<TreeComponent> sortedTrees = null;

	private bool chopped = false;
	private float startTime = 0f;
	private readonly int logsCreated = 2;

	public float workDuration = 4.2f; // seconds

	
	public ChopTreeAction () 
	{
		addPrecondition ("hasTool", true); // we need a tool to do this
		addPrecondition("isNight", false);  // not night
		addPrecondition("isThirsty", false); // watered
		addPrecondition("isHungry", false);  // fed
		addPrecondition ("hasLogs", false); // if we have logs we don't want more
		addEffect ("hasLogs", true);
	}
	
	public override void reset ()
	{
		chopped = false;
		startTime = 0;
		closest = null;
	}
	
	public override bool isDone ()
	{
		return chopped;
	}
	
	public override bool requiresInRange ()
	{
		return true; // yes we need to be near a tree
	}
	
	public override bool checkProceduralPrecondition (GameObject agent)
	{
		// find the nearest tree that we can chop
		if (trees == null)
		{
			trees = FindObjectsOfType(typeof(TreeComponent)) as TreeComponent[];
		}

		if (sortedTrees == null)
		{
			sortedTrees = trees.OrderBy(t => Vector3.Distance(transform.position, t.transform.position));
		}

		if (closest == null)
		{
			foreach (TreeComponent tree in sortedTrees)
			{
				if (tree.treeResource > 0 && tree.engaged != true)
				{
					closest = tree;
					break;
				}
			}
		}

		if (closest != null)
		{
			target = closest.gameObject;
		}
		
		return closest != null;
	}

	public override bool perform (GameObject agent)
	{
		if (tool == null)
		{
			tool = inventory.tool.GetComponent(typeof(ToolComponent)) as ToolComponent;
		}
		
		if (startTime == 0 && closest.engaged == false)
		{
			closest.engaged = true;
			startTime = Time.time;
			inventory.DetermineMood();
		}
		else if (startTime == 0 && closest.engaged == true)
		{
			return false;
		}

		if (!chopped) { animator.SetTrigger("chop"); }

		if (Time.time - startTime > workDuration) 
		{
			// finished chopping
			chopped = true;
			closest.engaged = false;
			animator.ResetTrigger("chop");
			inventory.hydration -= inventory.MoodModifier(hydrationConsumed);
			inventory.energy -= inventory.MoodModifier(energyConsumed);	
			inventory.numLogs += inventory.MoodModifier(logsCreated);
			closest.treeResource -= 1;
			DegradeTool(tool);
		}
		return true;
	}
}