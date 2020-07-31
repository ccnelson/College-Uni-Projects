// C NELSON UoH 2020
// Action script implementing GoapAction abstract class

using System.Linq;
using UnityEngine;

public class PickUpRawFoodAction : GoapAction
{
	private SupplyPileComponent[] supplyPiles = null;
	private SupplyPileComponent closest = null;
	IOrderedEnumerable<SupplyPileComponent> sortedSupplyPiles = null;

	private bool hasRawFood = false;
	private int noOfFood = 1;


	public PickUpRawFoodAction() 
	{
		addPrecondition ("hasRawFood", false); // don't collect rawfood if we already have some
		addEffect ("hasRawFood", true); // we now have rawfood
	}
	
	
	public override void reset ()
	{
		hasRawFood = false;
		closest = null;
	}
	
	public override bool isDone ()
	{
		return hasRawFood;
	}
	
	public override bool requiresInRange ()
	{
		return true; // need to be near a supply pile to pick up rawfood
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
				if (supply.numRawFood >= noOfFood)
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
		if (closest.numRawFood >= noOfFood) 
		{
			closest.numRawFood -= noOfFood;
			hasRawFood = true;
			inventory.numRawFood += noOfFood;
			
			return true;
		} 
		else 
		{
			// no raw food available, ran out before agent arrived
			return false;
		}
	}
}

