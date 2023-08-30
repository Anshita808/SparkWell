import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import TabNavigator from "./src/navigator/TabNavigator"; // Update the import path

const App = () => {
  return (
    <NavigationContainer>
      <TabNavigator/>
    </NavigationContainer>
  );
};

export default App;