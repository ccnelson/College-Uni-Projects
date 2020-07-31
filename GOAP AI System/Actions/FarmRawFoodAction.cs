// C NELSON UoH 2020
// Action script implementing GoapAction abstract class

using System.Linq;
using UnityEngine;

public class FarmRawFoodAction : GoapAction
{
	private ToolComponent tool = null;
	private FarmComponent[] farms = null;
	private FarmComponent closest = null;
	private IOrderedEnumerable<FarmComponent> sortedFarms = null;

	private bool farmed = false;
	private float startTime = 0f;
	private readonly int rawfoodCreated = 3;

	public float farmingDuration = 5f; // seconds

	public FarmRawFoodAction() 
	{
		addPrecondition ("hasTool", true); // we need a tool to do this
		addPrecondition("isNight", false);
		addPrecondition("isThirsty", false);
		addPrecondition("isHungry", false);
		addPrecondition ("hasRawFood", false); // if we already have rawfood don't need more
		addEffect ("hasRawFood", true);
	}
	
	public override void reset ()
	{
		farmed = false;
		startTime = 0;
		closest = null;
	}
	
	public override bool isDone ()
	{
		return farmed;
	}
	
	public override bool requiresInRange ()
	{
		return true; // yes we need to be near a farm resource
	}
	
	public override bool checkProceduralPrecondition (GameObject agent)
	{
		if (farms == null)
		{
			farms = FindObjectsOfType(typeof(FarmComponent)) as FarmComponent[];
		}

		if (sortedFarms == null)
		{
			sortedFarms = farms.OrderBy(t => Vector3.Distance(transform.position, t.transform.position));
		}

		if (closest == null)
		{
			foreach (FarmComponent farm in sortedFarms)
			{
				if (farm.farmResource > 0 && farm.engaged != true)
				{
					closest = farm;
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

		if (!farmed) { animator.SetTrigger("forge"); } // forge animation resembles farming

		if (Time.time - startTime > farmingDuration) 
		{
			// finished farming
			farmed = true;
			closest.engaged = false;
			animator.ResetTrigger("forge");
			inventory.hydration -= inventory.MoodModifier(hydrationConsumed);
			inventory.energy -= inventory.MoodModifier(energyConsumed);
			inventory.numRawFood += inventory.MoodModifier(rawfoodCreated);
			closest.farmResource -= 1;

			DegradeTool(tool);
			
		}
		return true;
	}
}


