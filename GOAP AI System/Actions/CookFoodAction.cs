// C NELSON UoH 2020
// Action script implementing GoapAction abstract class

using System.Linq;
using UnityEngine;

public class CookFoodAction : GoapAction
{
	private ToolComponent tool = null;
	private StoveComponent[] stoves = null;
	private StoveComponent closest = null;
	
	private bool cooked = false;
	private float startTime = 0f;
	private readonly int rawfoodConsumed = 1;
	private readonly int firewoodConsumed = 1;

	public float workDuration = 3.7f; // seconds

	public CookFoodAction() 
	{
		addPrecondition("hasTool", true); // we need a tool to do this
		addPrecondition("hasRawFood", true);  // has ingredients
		addPrecondition("hasFirewood", true);  // has firewood
		addPrecondition("isNight", false);  // not nighttime
		addPrecondition("isThirsty", false);  // is hydrated
		addEffect ("hasNewFood", true);
	}
	
	public override void reset ()
	{
		cooked = false;
		startTime = 0;
	}
	
	public override bool isDone ()
	{
		return cooked;
	}

	public override bool requiresInRange()
	{
		return true; // need to be near a stove
	}
	
	public override bool checkProceduralPrecondition (GameObject agent)
	{
		if (stoves == null)
		{
			stoves = FindObjectsOfType(typeof(StoveComponent)) as StoveComponent[];
		}
		
		if (closest == null)
		{
			closest = stoves.OrderBy(t => Vector3.Distance(transform.position, t.transform.position)).FirstOrDefault();
		}

		if (closest != null)
		{
			target = closest.gameObject;
		}
		
		return closest != null;
	}
	
	public override bool perform (GameObject agent)
	{
		if (inventory.numRawFood <= 0)
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

		if (!cooked) { animator.SetTrigger("cut"); }

		if (Time.time - startTime > workDuration) 
		{
			// finished cooking
			cooked = true;
			animator.ResetTrigger("cut");
			inventory.hydration -= inventory.MoodModifier(hydrationConsumed);
			//stats.energy -= energyConsumed; // unused as cook eats while working
			inventory.numRawFood -= inventory.MoodModifier(rawfoodConsumed);
			inventory.numFirewood -= inventory.MoodModifier(firewoodConsumed);

			DegradeTool(tool);
		}
		return true;
	}
}

