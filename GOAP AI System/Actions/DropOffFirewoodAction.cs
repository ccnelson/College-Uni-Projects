// C NELSON UoH 2020
// Action script implementing GoapAction abstract class
// Adapted from original script by
// Brent Owens (github.com/sploreg/goap)

using System.Linq;
using UnityEngine;

public class DropOffFirewoodAction : GoapAction
{
	private SupplyPileComponent[] supplyPiles = null;
	private SupplyPileComponent closest = null;

	private bool droppedOffFirewood = false;

	public DropOffFirewoodAction () 
	{
		addPrecondition ("hasFirewood", true); // need firewood
		addEffect ("hasFirewood", false); // now have no firewood
		addEffect ("woodcutterGoal", true); // delivered firewood
	}
	
	
	public override void reset ()
	{
		droppedOffFirewood = false;
	}
	
	public override bool isDone ()
	{
		return droppedOffFirewood;
	}
	
	public override bool requiresInRange ()
	{
		return true;
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
		//if (inventory.numFirewood <= 0)
		//{
		//	return false;
		//}
		
		closest.numFirewood += inventory.numFirewood;
		droppedOffFirewood = true;
		inventory.numFirewood = 0;
		
		return true;
	}
}
