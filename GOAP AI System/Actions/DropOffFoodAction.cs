// C NELSON UoH 2020
// Action script implementing GoapAction abstract class

using System.Linq;
using UnityEngine;

public class DropOffFoodAction : GoapAction
{
	private SupplyPileComponent[] supplyPiles = null;
	private SupplyPileComponent closest = null;

	private bool droppedOffFood = false;
	private readonly int noOfNewFood = 2;
	
	public DropOffFoodAction() 
	{
		addPrecondition ("hasNewFood", true); // need new food
		addEffect ("hasNewFood", false); // now have no food
		addEffect ("cookGoal", true); // delivered food
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
		return true; // need to be near a supply pile to drop off food
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
		// new food treated as condition (effect) instead of inventory item
		closest.numFood += noOfNewFood;
		droppedOffFood = true;
		
		return true;
	}
}
