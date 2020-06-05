// CHRIS NELSON NHC 2018
// object script is attached to 
// slowly rotates
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rotator : MonoBehaviour 
{
	void Update () 
	{
		transform.Rotate (new Vector3 (0, 0, 45) * Time.deltaTime);
	}
}
