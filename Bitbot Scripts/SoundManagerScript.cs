// CHRIS NELSON NHC 2018
// used to reference gameplay sound effects
// which are stored in Resources folder
// called from other scripts upon player actions
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SoundManagerScript : MonoBehaviour 
{
	public static AudioClip beeps;
	public static AudioClip hoover;
	public static AudioClip pickup;
	public static AudioClip player_died;
	public static AudioClip player_move;
	public static AudioClip scraping;
	public static AudioClip warning;
	public static AudioClip dooropen;
	public static AudioClip doorclose;
	public static AudioClip wirefix;
	static AudioSource audioSrc;
	
	void Start () 
	{
		beeps = Resources.Load<AudioClip> ("beeps");
		hoover = Resources.Load<AudioClip> ("hoover");
		pickup = Resources.Load<AudioClip> ("pickup");
		player_died = Resources.Load<AudioClip> ("player_died");
		player_move = Resources.Load<AudioClip> ("player_move");
		scraping = Resources.Load<AudioClip> ("scraping");
		warning = Resources.Load<AudioClip> ("warning");
		dooropen = Resources.Load<AudioClip> ("dooropen");
		doorclose = Resources.Load<AudioClip> ("doorclose");
		wirefix = Resources.Load<AudioClip> ("wirefix");
		audioSrc = GetComponent<AudioSource> ();
	}
	
	public static void Playsound (string clip)
	{
		switch (clip) {
		case "beeps":
			audioSrc.PlayOneShot (beeps);
			break;
		case "hoover":
			audioSrc.PlayOneShot (hoover);
			break;
		case "pickup":
			audioSrc.PlayOneShot (pickup);
			break;
		case "player_died":
			audioSrc.PlayOneShot (player_died);
			break;
		case "player_move":
			audioSrc.PlayOneShot (player_move);
			break;
		case "scraping":
			audioSrc.PlayOneShot (scraping);
			break;
		case "warning":
			audioSrc.PlayOneShot (warning);
			break;
		case "dooropen":
			audioSrc.PlayOneShot (dooropen);
			break;
		case "doorclose":
			audioSrc.PlayOneShot (doorclose);
			break;
		case "wirefix":
			audioSrc.PlayOneShot (wirefix);
			break;
		}
	}
}
