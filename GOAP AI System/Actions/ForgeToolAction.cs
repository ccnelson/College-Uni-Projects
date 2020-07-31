// C NELSON UoH 2020
// Action script implementing GoapAction abstract class
// Adapted from original script by
// Brent Owens (github.com/sploreg/goap)

using System.Linq;
using UnityEngine;

public class ForgeToolAction : GoapAction
{
	private ForgeComponent[] forges = null;
	private ForgeComponent closest = null;

	private bool forged = false;
	private float startTime = 0f;
	private readonly int oreConsumed = 1;
	private readonly int firewoodConsumed = 1;

	public float workDuration = 5f; // seconds

	public ForgeToolAction () 
	{
		addPrecondition ("hasOre", true);  // need ore
		addPrecondition("hasFirewood", true); // and firewood
		addPrecondition("isNight", false);  // and daylight
		addPrecondition("isThirsty", false);  // not thirsty
		addPrecondition("isHungry", false);  // or hungry
		addEffect ("hasNewTools", true);  // have created new tools
	}
	
	public override void reset ()
	{
		forged = false;
		startTime = 0;
	}
	
	public override bool isDone ()
	{
		return forged;
	}
	
	public override bool requiresInRange ()
	{
		return true; // need to be near a forge
	}
	
	public override bool checkProceduralPrecondition (GameObject agent)
	{
		if (forges == null)
		{
			forges = FindObjectsOfType(typeof(ForgeComponent)) as ForgeComponent[];
		}
		
		if (closest == null)
		{
			closest = forges.OrderBy(t => Vector3.Distance(transform.position, t.transform.position)).FirstOrDefault();
		}

		if (closest != null)
		{
			target = closest.gameObject;
		}

		return closest != null;
	}
	
	public override bool perform (GameObject agent)
	{	
		// check we have required components
		if ((inventory.numOre < oreConsumed) || (inventory.numFirewood < firewoodConsumed))
		{
			return false;
		}

		if (startTime == 0)
		{
			startTime = Time.time;
			inventory.DetermineMood();
		}

		if (!forged) { animator.SetTrigger("forge"); }

		if (Time.time - startTime > workDuration) 
		{
			// finished forging a tool
			forged = true;
			animator.ResetTrigger("forge");
			inventory.hydration -= inventory.MoodModifier(hydrationConsumed);
			inventory.energy -= inventory.MoodModifier(energyConsumed);
			inventory.numOre -= inventory.MoodModifier(oreConsumed);
			inventory.numFirewood -= inventory.MoodModifier(firewoodConsumed);
		}
		return true;
	}
}
