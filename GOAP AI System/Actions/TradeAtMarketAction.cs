// C NELSON UoH 2020
// Action script implementing GoapAction abstract class

using System.Linq;
using UnityEngine;

public class TradeAtMarketAction : GoapAction
{
	private MarketStallComponent[] workplaces = null;
	private MarketStallComponent closest = null;

	private bool worked = false;
	private float startTime = 0f;

	public float workDuration = 5f; // seconds

	
	public TradeAtMarketAction() 
	{
		addPrecondition("isNight", false);  // not night
		addPrecondition("isThirsty", false); // watered
		addPrecondition("isHungry", false);  // fed
		addPrecondition("hasWandered", true); // trader wanders
		addEffect("hasWandered", false);
		addEffect ("traderGoal", true);
	}
	
	public override void reset ()
	{
		worked = false;
		startTime = 0;
	}
	
	public override bool isDone ()
	{
		return worked;
	}
	
	public override bool requiresInRange ()
	{
		return true; // need to be near a market
	}
	
	public override bool checkProceduralPrecondition (GameObject agent)
	{
		// retrieve objects
		if (workplaces == null)
		{
			workplaces = FindObjectsOfType(typeof(MarketStallComponent)) as MarketStallComponent[];
		}

		// find closest 
		if (closest == null)
		{
			// linq 'OrderBy extension method for collections' finds nearest
			closest = workplaces.OrderBy(t => Vector3.Distance(transform.position, t.transform.position)).FirstOrDefault();
		}

		// ensure we have a value to set
		if (closest != null)
		{
			// set GoapAction target
			target = closest.gameObject;
		}

		return target != null;
	}

	public override bool perform (GameObject agent)
	{
		if (startTime == 0)
		{
			startTime = Time.time;
			inventory.DetermineMood();
		}

		if (!worked) { animator.SetTrigger("crossarms"); }

		if (Time.time - startTime > workDuration) 
		{
			// finished working
			worked = true;
			animator.ResetTrigger("crossarms");
			inventory.hydration -= inventory.MoodModifier(hydrationConsumed);
			inventory.energy -= inventory.MoodModifier(energyConsumed);	
		}
		return true;
	}
}