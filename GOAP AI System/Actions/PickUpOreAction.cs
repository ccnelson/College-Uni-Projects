// C NELSON UoH 2020
// Action script implementing GoapAction abstract class
// Adapted from original script by
// Brent Owens (github.com/sploreg/goap)

using System.Linq;
using UnityEngine;

public class PickUpOreAction : GoapAction
{
	private SupplyPileComponent[] supplyPiles = null;
	private SupplyPileComponent closest = null;
	IOrderedEnumerable<SupplyPileComponent> sortedSupplyPiles = null;

	private bool hasOre = false;
	private int noOfOre = 3;
	
	public PickUpOreAction () 
	{
		addPrecondition ("hasOre", false); // don't get a ore if we already have one
		addEffect ("hasOre", true); // we now have a ore
	}
	
	
	public override void reset ()
	{
		hasOre = false;
		closest = null;
	}
	
	public override bool isDone ()
	{
		return hasOre;
	}
	
	public override bool requiresInRange ()
	{
		return true; // need to be near a supply pile to pick up ore
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
				if (supply.numOre >= noOfOre)
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
		if (closest.numOre >= noOfOre) 
		{
			closest.numOre -= noOfOre;
			hasOre = true;
			inventory.numOre += noOfOre;
			
			return true;
		} 
		else 
		{
			//ore ran out before agent arrived
			return false;
		}
	}
}
