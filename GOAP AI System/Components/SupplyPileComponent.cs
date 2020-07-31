// C NELSON UoH 2020
// Component class for interactable objects
// Adapted from original script by
// Brent Owens (github.com/sploreg/goap)

using UnityEngine;
using TMPro;

public class SupplyPileComponent : MonoBehaviour
{
	private TextMeshPro text;

	// uses properties to monitor when variables change.
	// similar to inventory component.
	// prevents trying to update text every tick

	// tools
	private int m_numTools = 10;
	public int numTools
	{
		get { return m_numTools; }
		set
		{
			if (m_numTools == value) return;
			m_numTools = value;
			OnVariableChange?.Invoke();
		}
	}

	// logs
	private int m_numLogs = 5;
	public int numLogs
	{
		get { return m_numLogs; }
		set
		{
			if (m_numLogs == value) return;
			m_numLogs = value;
			OnVariableChange?.Invoke();
		}
	}

	// firewood
	private int m_numFirewood = 5;
	public int numFirewood
	{
		get { return m_numFirewood; }
		set
		{
			if (m_numFirewood == value) return;
			m_numFirewood = value;
			OnVariableChange?.Invoke();
		}
	}

	// ore
	private int m_numOre = 3;
	public int numOre
	{
		get { return m_numOre; }
		set
		{
			if (m_numOre == value) return;
			m_numOre = value;
			OnVariableChange?.Invoke();
		}
	}

	// rawfood
	private int m_numRawFood = 5;
	public int numRawFood
	{
		get { return m_numRawFood; }
		set
		{
			if (m_numRawFood == value) return;
			m_numRawFood = value;
			OnVariableChange?.Invoke();
		}
	}

	// food
	private int m_numFood = 5;
	public int numFood
	{
		get { return m_numFood; }
		set
		{
			if (m_numFood == value) return;
			m_numFood = value;
			OnVariableChange?.Invoke();
		}
	}

	// delegate event pair
	public delegate void OnVariableChangeDelegate();
	public event OnVariableChangeDelegate OnVariableChange;


	private void Start()
	{
		// initialise handler
		OnVariableChange += VariableChangeHandler;
		// get text component
		text = GetComponentInChildren<TextMeshPro>();
		// initialise text
		text.text = "Tools: \t" + numTools +
					"\nLogs: \t\t" + numLogs +
					"\nFirewood: \t" + numFirewood +
					"\nOre: \t\t" + numOre +
					"\nRawFood: \t" + numRawFood +
					"\nFood: \t" + numFood;
	}

	// event handler
	private void VariableChangeHandler()
	{
		// update text
		text.text = "Tools: \t" + numTools +
					"\nLogs: \t\t" + numLogs +
					"\nFirewood: \t" + numFirewood +
					"\nOre: \t\t" + numOre +
					"\nRawFood: \t" + numRawFood +
					"\nFood: \t" + numFood;
	}
}

