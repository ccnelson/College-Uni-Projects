// C NELSON UoH 2020
// Action script implementing GoapAction abstract class

using System;
using System.Linq;
using UnityEngine;

public class CollectResourcesAction : GoapAction
{
	private SupplyPileComponent[] supplies = null;
	private SupplyPileComponent closest = null;
	private IOrderedEnumerable<SupplyPileComponent> randomSortedSupplies = null;

	private bool collected = false;
	private float startTime = 0f;

	public float workDuration = 1f; // seconds

	public CollectResourcesAction() 
	{
		addPrecondition("isNight", false);  // not night
		addPrecondition("isThirsty", false); // watered
		addPrecondition("isHungry", false);  // fed
		addEffect("hasResources", true);
	}
	
	public override void reset ()
	{
		collected = false;
		startTime = 0;
		closest = null;
		randomSortedSupplies = null;
	}
	
	public override bool isDone ()
	{
		return collected;
	}
	
	public override bool requiresInRange ()
	{
		return true;
	}
	
	public override bool checkProceduralPrecondition (GameObject agent)
	{
		if (supplies == null)
		{
			supplies = FindObjectsOfType(typeof(SupplyPileComponent)) as SupplyPileComponent[];
		}


		if (randomSortedSupplies == null)
		{
			// use linq orderby new guid to generate random order
			randomSortedSupplies = from s in supplies orderby Guid.NewGuid() ascending select s; 
		}

		if (closest == null)
		{
			foreach (SupplyPileComponent supply in randomSortedSupplies)
			{
				if (supply.numFirewood > 10 || supply.numFood > 10 || 
					supply.numLogs > 10 || supply.numOre > 10 || 
					supply.numRawFood > 10)
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
			// if supply pile has more than 10 of any resource
			// take half

			if (closest.numFirewood > 10)
			{
				inventory.numFirewood += (closest.numFirewood / 2);
				closest.numFirewood = (closest.numFirewood / 2);
			}

			if (closest.numLogs > 10)
			{
				inventory.numLogs += (closest.numLogs / 2);
				closest.numLogs = (closest.numLogs / 2);
			}

			if (closest.numFood > 10)
			{
				inventory.numFood += (closest.numFood / 2);
				closest.numFood = (closest.numFood / 2);
			}

			if (closest.numOre > 10)
			{
				inventory.numOre += (closest.numOre / 2);
				closest.numOre = (closest.numOre / 2);
			}

			if (closest.numRawFood > 10)
			{
				inventory.numRawFood += (closest.numRawFood / 2);
				closest.numRawFood = (closest.numRawFood / 2);
			}

			collected = true;
			
		}
		return true;
	}
}