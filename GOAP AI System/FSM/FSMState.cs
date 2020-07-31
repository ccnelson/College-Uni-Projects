// C NELSON UoH 2020
// FSM State Script
// Original script by
// Brent Owens (github.com/sploreg/goap)

using UnityEngine;
using System.Collections;

public interface FSMState 
{
	
	void Update (FSM fsm, GameObject gameObject);
}

