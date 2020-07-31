// C NELSON UoH 2020
// Action script implementing GoapAction abstract class

using System.Linq;
using UnityEngine;

public class DropOffRawFoodAction : GoapAction
{
	private SupplyPileComponent[] supplyPiles = null;
	private SupplyPileComponent closest = null;

	private bool droppedOffFood = false;
	
	public DropOffRawFoodAction() 
	{
		addPrecondition ("hasRawFood", true); // need rawfood to drop off
		addEffect ("hasRawFood", false); // now have no raw food
		addEffect ("farmerGoal", true); // we delivered raw food
	}
	
	public override void reset ()
	{
		droppedOffFood = false;
	}
	
	public override bool isDone ()
	{
		return droppedOffFood;
	}
	
	public override bool requiresInRange ()
	{
		return true; // need to be near a supply pile to drop off rawfood
	}
	
	public override bool checkProceduralPrecondition (GameObject agent)
	{
		if (supplyPiles == null)
		{
			supplyPiles = FindObjectsOfType(typeof(SupplyPileComponent)) as SupplyPileComponent[];
		}

		if (closest == null)
		{
			closest = supplyPiles.OrderBy(t => Vector3.Distance(transform.position, t.transform.position)).FirstOrDefault();
		}

		if (closest != null)
		{
			target = closest.gameObject;
		}

		return closest != null;
	}
	
	public override bool perform (GameObject agent)
	{
		closest.numRawFood += inventory.numRawFood;
		droppedOffFood = true;
		inventory.numRawFood = 0;
		
		return true;
	}
}
