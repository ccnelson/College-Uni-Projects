// C NELSON UoH 2020
// Action script implementing GoapAction abstract class

using UnityEngine;


public class SleepAction : GoapAction
{
	public HomeComponent home;
	private Renderer[] myRenderer = null;

	private bool slept = false;
	private bool rendereractive = true;  // to track renderer rendering
	private float startTime = 0f;
	private float snoozeModified;
	private readonly int energyRegainedSleeping = 1;
	public float snoozeDuration = 1f;


	public SleepAction() 
	{
		addPrecondition("isNight", true);  // only sleep at night
		addEffect("blacksmithGoal", true);  // satisifies everyones goals
		addEffect("loggerGoal", true);
		addEffect("woodcutterGoal", true);
		addEffect("minerGoal", true);
		addEffect("cookGoal", true);
		addEffect("farmerGoal", true);
		addEffect("peasantGoal", true);
		addEffect("traderGoal", true);
		addEffect("redistributorGoal", true);

	}
	
	public override void reset ()
	{
		startTime = 0;
		slept = false;
		rendereractive = true;
	}
	
	public override bool isDone ()
	{
		return slept;
	}
	
	public override bool requiresInRange ()
	{
		return true;
	}
	
	public override bool checkProceduralPrecondition (GameObject agent)
	{
		target = home.gameObject; // agent assigned home via gui sleep script component
		return true;
	}
	
	public override bool perform (GameObject agent)
	{
		// get renderer prior to sleeping, this ensures agents state is correct.
		// i.e. agents tool may have broken and despawned
		myRenderer = GetComponentsInChildren<Renderer>();

		if (rendereractive == true && inventory.localtime.timeofday == TimeTracker.TimeOfDay.NIGHT)
		{
			// make agent disappear into home
			foreach (Renderer r in myRenderer)
			{
				r.enabled = false;
			}
			rendereractive = false;
		}

		if (inventory.localtime.timeofday != TimeTracker.TimeOfDay.NIGHT) 
		{
			if (startTime == 0)
			{
				startTime = Time.time;
				inventory.DetermineMood();
				// mood effect on snooze amount
				snoozeModified = inventory.MoodModifier(snoozeDuration);
			}

			if (Time.time - startTime > snoozeModified) // each agent can lie-in
			{
				slept = true;
				inventory.energy += energyRegainedSleeping;
				foreach (Renderer r in myRenderer)
				{
					r.enabled = true;
				}
				rendereractive = true;
			}
		}
		return true;
	}
}
