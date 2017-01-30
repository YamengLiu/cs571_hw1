using UnityEngine;
using System.Collections;

public class Script : MonoBehaviour {
    //Initialization
    private float playerHealth = 100.0f;

    private float powerUpAmount = 90.9f;

    private bool isDangerZone = false;

	// Use this for initialization
	void Start () {
        //Cut the playerHealth to half and print out
        playerHealth = playerHealth * 0.5f;
        print("printHealth now: " + playerHealth);

        //The player gets the power up added
        float powerUp = 1;
        powerUpAmount += powerUp;
        print("powerUpAmount now: " + powerUpAmount);

        //Determine if the player is at the Danger Zone
        if(playerHealth < 20f)
        {
            isDangerZone = true;
        }
        print("isDangerZone is " + isDangerZone);

        //Increment health one point in three different ways
        playerHealth += 1;
        playerHealth++;
        playerHealth = playerHealth + 1;

        //Show an integer, not a float in the console
        int health = (int)playerHealth;
        print("printHealth now: " + health);

        //Decide whether playerHealth is an even number
        bool isEven = false;
        if(health%2 == 1)
        {
            isEven = true;
        }

        if(isEven == true) { print("playerHealth is an even number."); }
        else { print("playerHealth is an odd number."); }
      
    }

}
