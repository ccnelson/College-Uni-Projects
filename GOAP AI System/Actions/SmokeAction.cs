// C NELSON UoH 2020
// Action script implementing GoapAction abstract class

using UnityEngine;


public class SmokeAction : GoapAction
{
	private bool smoked = false;
	private float startTime;
	private readonly float smokeDuration = 3f;


	public SmokeAction() 
	{
		addPrecondition("isNight", false);
		addEffect ("blacksmithGoal", true);
		addEffect("loggerGoal", true);
		addEffect("woodcutterGoal", true);
		addEffect("minerGoal", true);
		addEffect("cookGoal", true);
		addEffect("farmerGoal", true);
		addEffect("peasantGoal", true);
		addEffect("traderGoal", true);
		addEffect("redistributorGoal", true);

		// smoke action allows any agent to satisfy their goal,
		// however it is the most expensive method available
		// and agents will only choose this method if unable
		// to satisfy their goals via other means.
	}
	
	public override void reset ()
	{
		smoked = false;
		startTime = 0;
	}
	
	public override bool isDone ()
	{
		return smoked;
	}
	
	public override bool requiresInRange ()
	{
		return false; // can smoke anywhere
	}
	
	public override bool checkProceduralPrecondition (GameObject agent)
	{
		return true;
	}
	
	public override bool perform (GameObject agent)
	{
		if (startTime == 0)
		{
			startTime = Time.time;
			if (!smoked) { animator.SetTrigger("smoke"); }
			inventory.DetermineMood();
		}

		if (Time.time - startTime > smokeDuration)
		{
			smoked = true;
			animator.ResetTrigger("smoke");			
		}
		return true;
	}
	
}
