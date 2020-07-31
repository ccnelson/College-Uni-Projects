// C NELSON UoH 2020
// Action script implementing GoapAction abstract class

using System.Linq;
using UnityEngine;

public class PickUpFoodAction : GoapAction
{
	private SupplyPileComponent[] supplyPiles = null;
	private SupplyPileComponent closest = null;
	IOrderedEnumerable<SupplyPileComponent> sortedSupplyPiles = null;

	private bool hasFood = false;
	private readonly int noOfFood = 1;
	
	public PickUpFoodAction() 
	{
		addPrecondition ("hasFood", false); // don't get food if we already have it
		addEffect ("hasFood", true); // we now have a food
	}
	
	
	public override void reset ()
	{
		hasFood = false;
		closest = null;
	}
	
	public override bool isDone ()
	{
		return hasFood;
	}
	
	public override bool requiresInRange ()
	{
		return true; // need to be near a supply pile to pick up food
	}
	
	public override bool checkProceduralPrecondition (GameObject agent)
	{
		if (supplyPiles == null)
		{
			supplyPiles = FindObjectsOfType(typeof(SupplyPileComponent)) as SupplyPileComponent[];
		}

		if (sortedSupplyPiles == null)
		{
			sortedSupplyPiles = supplyPiles.OrderBy(t => Vector3.Distance(transform.position, t.transform.position));
		}

		if (closest == null)
		{
			foreach (SupplyPileComponent supply in sortedSupplyPiles)
			{
				if (supply.numFood >= noOfFood)
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
		if (closest.numFood >= noOfFood)
		{
			closest.numFood -= noOfFood;
			hasFood = true;
			inventory.numFood += noOfFood;

			return true;
		}  
		else 
		{
			// no food available, somebody got there first
			return false;
		}
	}
}
