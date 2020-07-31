// C NELSON UoH 2020
// Action script implementing GoapAction abstract class

using System.Linq;
using UnityEngine;

public class DistributeResourcesAction : GoapAction
{
	private SupplyPileComponent[] supplies = null;
	private SupplyPileComponent closest = null;
	private IOrderedEnumerable<SupplyPileComponent> sortedSupplies = null;

	private bool distributed = false;
	private float startTime = 0f;

	public float workDuration = 1f; // seconds

	
	public DistributeResourcesAction() 
	{
		addPrecondition("isNight", false);  // not night
		addPrecondition("isThirsty", false); // watered
		addPrecondition("isHungry", false);  // fed
		addPrecondition("hasResources", true);
		addEffect ("redistributorGoal", true);
		addEffect("hasResources", false);
	}
	
	public override void reset ()
	{
		distributed = false;
		startTime = 0;
		closest = null;
		sortedSupplies = null;
	}
	
	public override bool isDone ()
	{
		return distributed;
	}
	
	public override bool requiresInRange ()
	{
		return true; // need to be near supply pile
	}
	
	public override bool checkProceduralPrecondition (GameObject agent)
	{
		// find furthest supply pile

		if (supplies == null)
		{
			supplies = FindObjectsOfType(typeof(SupplyPileComponent)) as SupplyPileComponent[];
		}


		if (sortedSupplies == null)
		{
			sortedSupplies = supplies.OrderByDescending(t => Vector3.Distance(transform.position, t.transform.position));
		}

		if (closest == null)
		{
			foreach (SupplyPileComponent supply in sortedSupplies)
			{
				if (supply.numFirewood < 10 || supply.numFood < 10 || 
					supply.numLogs < 10 || supply.numOre < 10 || 
					supply.numRawFood < 10)
				{
					closest = supply;
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
		if (startTime == 0)
		{
			startTime = Time.time;
			inventory.DetermineMood();
		}

		if (Time.time - startTime > workDuration) 
		{
			closest.numFirewood += inventory.numFirewood;
			closest.numFood += inventory.numFood;
			closest.numLogs += inventory.numLogs;
			closest.numOre += inventory.numOre;
			closest.numRawFood += inventory.numRawFood;

			inventory.numFirewood = 0;
			inventory.numFood = 0;
			inventory.numLogs = 0;
			inventory.numOre = 0;
			inventory.numRawFood = 0;

			inventory.energy -= inventory.MoodModifier(energyConsumed);
			inventory.hydration -= inventory.MoodModifier(hydrationConsumed);

			// finished distributing
			distributed = true;
		}
		return true;
	}
}