// CHRIS NELSON NHC 2018
// adjust light intensity
// at random intervals
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RandomFlash : MonoBehaviour 
{
    public Light myLight;
    private float delay; 
    private float minIntensity; 
    private float maxIntensity; 
    private float timeElapsed;
 
    private void Start()
    {
        myLight.intensity = maxIntensity;
		delay = 0.1f;
		minIntensity = 0f;
		maxIntensity = 1f;
    }
 
    private void Update()
    {
        timeElapsed += Time.deltaTime;
        if (timeElapsed >= delay)
        {
            timeElapsed = 0;
            ToggleLight();
			delay = Random.Range(0.1f, 0.5f);
        }
    }
 
    public void ToggleLight()
    {
        if (myLight.intensity == minIntensity)
        {
            myLight.intensity = maxIntensity;
        }
        else if (myLight.intensity == maxIntensity)
        {
            myLight.intensity = minIntensity;
        }
    }
}
