// CHRIS NELSON NHC 2018
// adjust light intensity
// at regular intervals
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LightFlash : MonoBehaviour 
{
    public float delay; // time between flashes 
    public float minIntensity; // flash off brightness
    public float maxIntensity; // flash on brightness
    private Light myLight;      // holds ref to light
    private float timeElapsed;  // counter 
 
    private void Start()
    {
        myLight = GetComponent<Light>(); // gets light it is attached to
        myLight.intensity = maxIntensity;
    }
 
    private void Update()
    {
        timeElapsed += Time.deltaTime;
        if(timeElapsed >= delay)
        {
            timeElapsed = 0;
            ToggleLight();
        }
    }
 
    public void ToggleLight()
    {
        if(myLight.intensity == minIntensity)
        {
            myLight.intensity = maxIntensity;
        }
        else if(myLight.intensity == maxIntensity)
        {
            myLight.intensity = minIntensity;
        }
    }
}
