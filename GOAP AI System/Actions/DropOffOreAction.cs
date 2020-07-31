// C NELSON UoH 2020
// Action script implementing GoapAction abstract class
// Adapted from original script by
// Brent Owens (github.com/sploreg/goap)

using System.Linq;
using UnityEngine;

public class DropOffOreAction : GoapAction
{
	private SupplyPileComponent[] supplyPiles = null;
	private SupplyPileComponent closest = null;

	private bool droppedOffOre = false;
	
	public DropOffOreAction () 
	{
		addPrecondition ("hasOre", true); // need ore
		addEffect ("hasOre", false); // now have no ore
		addEffect ("minerGoal", true); // delivered ore
	}
	
	public override void reset ()
	{
		droppedOffOre = false;
	}
	
	public override bool isDone ()
	{
		return droppedOffOre;
	}
	
	public override bool requiresInRange ()
	{
		return true; // need to be near
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
		closest.numOre += inventory.numOre;
		droppedOffOre = true;
		inventory.numOre = 0;
		
		return true;
	}
}
