// CHRIS NELSON NHC 2018
// door control system
// uses bool value held in 
// objects animator
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DoorScript : MonoBehaviour 
{
	Animator anim;

	void Start () 
    {
		anim = GetComponent<Animator> ();
	}
	
    // player near door - open door
	private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.name == "player")
        {        
            anim.SetBool ("player_near", true);
            SoundManagerScript.Playsound ("dooropen");
        }
    }

    // player not near door, close door
	private void OnTriggerExit2D(Collider2D collision)
    {
        if (collision.gameObject.name == "player")
        {        
            anim.SetBool ("player_near", false);
            SoundManagerScript.Playsound ("doorclose");
        }
    }
}
