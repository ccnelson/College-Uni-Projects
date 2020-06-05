// CHRIS NELSON NHC 2018
// player has finished demo
// quit application on input
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CompletedScreenScript : MonoBehaviour 
{	
	void Update () {
		if (Input.anyKeyDown == true) 
		{
			Application.Quit();
		}
	}
}
