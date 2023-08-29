// src/navigation/AppNavigator.js
import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import UserProfileScreen from "./src/screens/UserProfileScreen";
import GoalSettingScreen from "./src/screens/GoalSettingScreen";

const Stack = createStackNavigator();

const AppNavigator = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="UserProfile">
        <Stack.Screen name="UserProfile" component={UserProfileScreen} />
        <Stack.Screen name="GoalSetting" component={GoalSettingScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default AppNavigator;
