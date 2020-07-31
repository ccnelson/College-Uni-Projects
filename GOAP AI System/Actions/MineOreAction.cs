// C NELSON UoH 2020
// Action script implementing GoapAction abstract class
// Adapted from original script by
// Brent Owens (github.com/sploreg/goap)

using System.Linq;
using UnityEngine;

public class MineOreAction : GoapAction
{
	private ToolComponent tool = null;
	private IronRockComponent[] rocks = null;
	private IronRockComponent closest = null;
	private IOrderedEnumerable<IronRockComponent> sortedRocks = null;

	private bool mined = false;
	private float startTime = 0f;
	private readonly int oreCreated = 3;

	public float workDuration = 4f; // seconds

	public MineOreAction () 
	{
		addPrecondition ("hasTool", true); // we need a tool to do this
		addPrecondition("isNight", false); // not night
		addPrecondition("isThirsty", false); // not thirsty
		addPrecondition("isHungry", false);  // not hungry
		addPrecondition ("hasOre", false); // if we already have ore we don't need more
		addEffect ("hasOre", true);
	}
	
	public override void reset ()
	{
		mined = false;
		startTime = 0;
		closest = null;
	}
	
	public override bool isDone ()
	{
		return mined;
	}
	
	public override bool requiresInRange ()
	{
		return true; // need to be near a rock
	}
	
	public override bool checkProceduralPrecondition (GameObject agent)
	{
		if (rocks == null)
		{
			rocks = FindObjectsOfType(typeof(IronRockComponent)) as IronRockComponent[];
		}
		
		if (sortedRocks == null)
		{
			sortedRocks = rocks.OrderBy(t => Vector3.Distance(transform.position, t.transform.position));
		}

		if (closest == null)
		{
			foreach (IronRockComponent rock in sortedRocks)
			{
				if (rock.rockResource > 0 && rock.engaged != true)
				{
					closest = rock;
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

		if (!mined) { animator.SetTrigger("mine"); }

		if (Time.time - startTime > workDuration) 
		{
			// finished mining
			mined = true;
			closest.engaged = false;
			animator.ResetTrigger("mine");
			inventory.hydration -= inventory.MoodModifier(hydrationConsumed);
			inventory.energy -= inventory.MoodModifier(energyConsumed);
			inventory.numOre += inventory.MoodModifier(oreCreated);
			closest.rockResource -= 1;

			DegradeTool(tool);
		}
		return true;
	}
}


