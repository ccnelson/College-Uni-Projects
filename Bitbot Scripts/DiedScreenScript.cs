// CHRIS NELSON NHC 2018
// player has died
// change scene on input
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class DiedScreenScript : MonoBehaviour 
{	
	void Update () 
	{
		if (Input.GetKey (KeyCode.Y)) 
		{
			SceneManager.LoadScene("main", LoadSceneMode.Single);
		}
		else if (Input.GetKey (KeyCode.N)) 
		{
			Application.Quit();
		}
	}
}
