// C NELSON UoH 2020
// Action script implementing GoapAction abstract class
// Adapted from original script by
// Brent Owens (github.com/sploreg/goap)

using System.Linq;
using UnityEngine;

public class ChopFirewoodAction : GoapAction
{
	// objects
	private ToolComponent tool = null;
	private ChoppingBlockComponent[] blocks = null;
	private ChoppingBlockComponent closest = null;
	// internal variables
	private bool chopped = false;
	private float startTime = 0f;
	private readonly int logsConsumed = 1;
	private readonly int firewoodCreated = 5;
	// public variables
	public float workDuration = 3.3f; // seconds

	public ChopFirewoodAction()
	{
		addPrecondition("hasTool", true); // we need a tool to do this
		addPrecondition("hasLogs", true);  // need logs
		addPrecondition("isNight", false); // not at night
		addPrecondition("isThirsty", false); // hydrated
		addPrecondition("isHungry", false);  // fed
		addPrecondition("hasFirewood", false); // if we have firewood we don't want more
		addEffect("hasFirewood", true);
	}

	public override void reset()
	{
		chopped = false;
		startTime = 0;
	}

	public override bool isDone()
	{
		return chopped;
	}

	public override bool requiresInRange()
	{
		return true; // yes we need to be near a chopping block
	}

	public override bool checkProceduralPrecondition(GameObject agent)
	{
		// retreive objects
		if (blocks == null)
		{
			blocks = FindObjectsOfType(typeof(ChoppingBlockComponent)) as ChoppingBlockComponent[];
		}
		
		// find closest 
		if (closest == null)
		{
			// linq 'OrderBy extension method for collections' finds nearest
			closest = blocks.OrderBy(t => Vector3.Distance(transform.position, t.transform.position)).FirstOrDefault();
		}
		
		// ensure we have a value to set
		if (closest != null)
		{
			// set GoapAction target
			target = closest.gameObject;
		}

		// return our success
		return closest != null;
	}

	public override bool perform(GameObject agent)
	{
		// check inventory first
		if (inventory.numLogs <= 0)
		{
			return false;
		}

		if (tool == null)
		{
			tool = inventory.tool.GetComponent(typeof(ToolComponent)) as ToolComponent;
		}
		
		if (startTime == 0)
		{
			startTime = Time.time;
			inventory.DetermineMood();
		}

		// run animation while action continues
		if (!chopped) { animator.SetTrigger("cut"); }

		if (Time.time - startTime > workDuration)
		{
			// finished chopping
			chopped = true;
			// reset animation trigger
			animator.ResetTrigger("cut");
			// update stats
			inventory.hydration -= inventory.MoodModifier(hydrationConsumed);
			inventory.energy -= inventory.MoodModifier(energyConsumed);
			//inventory.numLogs -= WorkMoodActionsConsume(logsConsumed);
			inventory.numLogs -= inventory.MoodModifier(logsConsumed);
			//inventory.numFirewood += WorkMoodActionsCreate(firewoodCreated);
			inventory.numFirewood += inventory.MoodModifier(firewoodCreated);
			// tool degrades as used
			DegradeTool(tool);
		}
		return true;
	}
}

