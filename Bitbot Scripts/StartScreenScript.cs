// CHRIS NELSON NHC 2018
// welcome player to game
// anykey starts game
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class StartScreenScript : MonoBehaviour 
{
	void Update () 
	{
		if (Input.anyKeyDown == true) 
		{
			SceneManager.LoadScene("main", LoadSceneMode.Single);
		}
	}
}
