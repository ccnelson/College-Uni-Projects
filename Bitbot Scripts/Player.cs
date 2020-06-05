// CHRIS NELSON NHC 2018
// sub class of character 
// main game functionality 
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class Player : Character 
{
	// prepare variables
	Animator anim;
	public static bool has_vac;
	public static bool unlocked_vac;
	public static bool has_bull;
	public static bool unlocked_bull;
	public static bool has_tool;
	public static bool unlocked_tool;
	public static bool has_key;
	
	// GUI stuff
	private int health;
	private int resources;
	public Text holderText;

	// variables to access instances & bodies of crates & parts
	// we wish to alter their pyhsics based on players active tool
	public GameObject[] crates;
	public Rigidbody2D crate_body;
	public GameObject[] parts;
	public BoxCollider2D parts_body;

	// screen flash variable
	public Color myColour;

	// morbid variable
	public bool dead;

	void Start () 
	{
		dead = false;
		crates = GameObject.FindGameObjectsWithTag("crates"); 	// gets a list of all crates
		parts = GameObject.FindGameObjectsWithTag("parts");     // likewise for parts
		anim = GetComponent<Animator> (); 			// gets this objects animator
		has_vac = false; 				// initial values of tools / key
		unlocked_vac = false;
		has_bull = false;
		unlocked_bull = false;
		has_tool = false;
		unlocked_tool = false;
		has_key = false;
		HideVac(); // hide tools
		HideBull();
		HideTool();
		// gui stuff
		health = 10;
		resources = 0;
		SetGUIText ();
		// these numbers come from editor lighting settings - RGB & current brightness
		myColour = new Color (0.1838235F, 0.1865268F, 0.1865268F, 0.1865268F);
		// i like to think this is bitbots alarm clock
		SoundManagerScript.Playsound ("beeps");
	}
	
	protected override void Update () 	// override parent
	{
		if (health <= 0)
		{
			dead = true; // first things first, is player dead?
		}
		if (dead == true)
		{
			SceneManager.LoadScene("died", LoadSceneMode.Single); // trigger died screen
		}
		GetInput(); // get input responds to player input
		base.Update(); // runs parent (character) class update (applies movement)
	}

	// player interaction via keyboard
	private void GetInput()
	{
		// reset values
		direction = Vector3.zero;
		rot = Vector3.zero;
		anim.SetBool ("moving", false);
		// set speed
		speed = 2.5f;
		// WASD controls - we dont was else if, as players 
		// should be able to bank sideways
		if (Input.GetKey(KeyCode.W)) 
		{ 
			direction += Vector3.up;
			anim.SetBool ("moving", true);
			SoundManagerScript.Playsound ("player_move");
		}
		if (Input.GetKey(KeyCode.A)) 
		{
			rot += new Vector3 (0, 0, 180); 
			anim.SetBool ("moving", true);
			SoundManagerScript.Playsound ("player_move");
		}
		if (Input.GetKey(KeyCode.S)) 
		{ 
			direction += Vector3.down;
			anim.SetBool ("moving", true);
			SoundManagerScript.Playsound ("player_move");
		}
		if (Input.GetKey(KeyCode.D)) 
		{ 
			rot += new Vector3 (0, 0, -180);
			anim.SetBool ("moving", true);
			SoundManagerScript.Playsound ("player_move");
		}
		// booster
		if (Input.GetKey(KeyCode.Q)) 
		{ 
			speed = speed * 2;
		}
		// show vacuum
		if (Input.GetKeyDown(KeyCode.V)) 
		{ 
			if (unlocked_vac == true)
			{
				SoundManagerScript.Playsound ("pickup");
				has_vac = !has_vac;
				if (has_vac == false)
				{	
					HideVac();
				}
				if (has_vac == true)
				{
					HideBull();
					HideTool();
					has_bull = false;
					has_tool = false;
					ShowVac();
				}
			}	
		}
		// show bulldozer
		if (Input.GetKeyDown(KeyCode.B)) 
		{ 
			if (unlocked_bull == true)
			{
				SoundManagerScript.Playsound ("pickup");
				has_bull = !has_bull;
				if (has_bull == false)
				{	
					HideBull();
				}
				if (has_bull == true)
				{
					HideVac();
					HideTool();
					has_vac = false;
					has_tool = false;
					ShowBull();
				}
			}
		}

		// show tool
		if (Input.GetKeyDown(KeyCode.C)) 
		{ 
			if (unlocked_tool == true)
			{
				SoundManagerScript.Playsound ("pickup");
				has_tool = !has_tool;
				if (has_tool == false)
				{	
					HideTool();
				}
				if (has_tool == true)
				{
					HideVac();
					HideBull();
					has_vac = false;
					has_bull = false;
					ShowTool();
				}
			}
		}
		// end of player keyboard interactions
	}

	void SetGUIText () // builds a string for GUI display linked in editor
	{
		holderText.text = "HEALTH: " + health.ToString() + "\n\nRESOURCES: " + resources.ToString() + "\n\nKEY: " + has_key.ToString();
	}

	// COLLISIONS
	// note - some collisions have a pause (screen flash red) 
	// using waitforseconds, which yield a return object, 
	// therefor method is ienumerator
	IEnumerator OnTriggerEnter2D(Collider2D collision)
    {
        // green blob collisions
		if (collision.gameObject.CompareTag ("globs"))
        {
			if (has_vac == true)
			{
				SoundManagerScript.Playsound ("hoover");
				collision.gameObject.SetActive (false);
				resources = resources + 1;
				SetGUIText();
			}
			if (has_vac == false)
			{
				health = health - 1;
				SetGUIText();
				SoundManagerScript.Playsound ("warning");
				RenderSettings.ambientLight = Color.red;
				yield return new WaitForSeconds(0.3F);
				RenderSettings.ambientLight = myColour;
			} 
        }
		// part collisions
		if (collision.gameObject.CompareTag ("parts"))
        {
			if (has_vac == true)
			{
				SoundManagerScript.Playsound ("hoover");
				collision.gameObject.SetActive (false);
				resources = resources + 2;
				SetGUIText();
			}
        }
		// wire collisions
		if (collision.gameObject.CompareTag ("wires"))
        {
			if (has_tool == true)
			{
				SoundManagerScript.Playsound ("wirefix");
				collision.gameObject.SetActive (false);
				RenderSettings.ambientLight = Color.blue;
				yield return new WaitForSeconds(0.2F);
				RenderSettings.ambientLight = myColour;
				
			}
			if (has_tool == false)
			{
				health = health - 15; // instant death if you hit a live wire
				SetGUIText();
				RenderSettings.ambientLight = Color.red;
				yield return new WaitForSeconds(1F);
				RenderSettings.ambientLight = myColour;
			}
        }

		// pickup collisions (unlocking tools)
		if (collision.gameObject.CompareTag ("bull_pickup"))
        {
			collision.gameObject.SetActive (false);
			has_bull = true;
			unlocked_bull = true;
			ShowBull(); // in demo there is predetermined order of tool unlocks
			HideVac();  // but future levels may change order
			HideTool(); // so hide other tools
			has_vac = false;
			has_tool = false;
			SoundManagerScript.Playsound ("pickup");
        }
		if (collision.gameObject.CompareTag ("vac_pickup"))
        {
			collision.gameObject.SetActive (false);
			has_vac = true;
			unlocked_vac = true;
			ShowVac();
			HideBull();
			HideTool();
			has_bull = false;
			has_tool = false;
			SoundManagerScript.Playsound ("pickup");
        }
		if (collision.gameObject.CompareTag ("tool_pickup"))
        {
			collision.gameObject.SetActive (false);
			has_tool = true;
			unlocked_tool = true;
			ShowTool();
			HideBull();
			HideVac();
			has_bull = false;
			has_vac = false;
			SoundManagerScript.Playsound ("pickup");
        }
		if (collision.gameObject.CompareTag ("key"))
        {
			SoundManagerScript.Playsound ("pickup");
			collision.gameObject.SetActive (false);
			has_key = true;
			SetGUIText();
        }
		// exit collisions
		if (collision.gameObject.CompareTag ("exit"))
        {
			if (has_key == true)
			{
				SceneManager.LoadScene("completed", LoadSceneMode.Single);
			}
        }
    }

	// internal helper functions
	void ShowVac()
	{
		// tools are always present, hiding rescales to zero
		// show returns a tools scale to 1
		GameObject.Find ("vacuum").transform.localScale = new Vector3(1, 1, 1);
		// cycle thru all parts
		foreach (GameObject part in parts)
		{
			// turning triggers on, this changes each part
			// from a solid object to something we can pickup
			parts_body = part.GetComponent<BoxCollider2D>();
			parts_body.isTrigger = true;
		}
	}
	void HideVac()
	{
		GameObject.Find ("vacuum").transform.localScale = new Vector3(0, 0, 0);
		foreach (GameObject part in parts)
		{
			parts_body = part.GetComponent<BoxCollider2D>();
			parts_body.isTrigger = false;
		}
	}
	void ShowBull()
	{
		GameObject.Find ("bulldoze").transform.localScale = new Vector3(1, 1, 1);
		foreach (GameObject crate in crates)
		{
			// as with parts in show_vac, but change physics of
			// crates from static to dynamic, so we can push
			// around with bulldozer
			crate_body = crate.GetComponent<Rigidbody2D>();
			crate_body.bodyType = RigidbodyType2D.Dynamic;
		}
	}
	void HideBull()
	{
		GameObject.Find ("bulldoze").transform.localScale = new Vector3(0, 0, 0);
		foreach (GameObject crate in crates)
		{
			crate_body = crate.GetComponent<Rigidbody2D>();
			crate_body.bodyType = RigidbodyType2D.Static;
		}
	}

	void ShowTool()
	{
		GameObject.Find ("tool").transform.localScale = new Vector3(1, 1, 1);
	}
	void HideTool()
	{
		GameObject.Find ("tool").transform.localScale = new Vector3(0, 0, 0);
	}

}
