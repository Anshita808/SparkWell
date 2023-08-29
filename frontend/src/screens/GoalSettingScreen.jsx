import React, { useState } from "react";
import { View, Text, TextInput, Button, StyleSheet } from "react-native";

const GoalSettingScreen = ({ navigation }) => {
  const [goal, setGoal] = useState("");

  const handleSaveGoal = () => {
    navigation.goBack(); 
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Goal Setting</Text>
      <TextInput
        style={styles.input}
        placeholder="Enter your goal"
        value={goal}
        onChangeText={setGoal}
      />
      <Button title="Save Goal" onPress={handleSaveGoal} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    justifyContent: "center",
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
  },
  input: {
    marginBottom: 10,
    padding: 10,
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 5,
  },
});

export default GoalSettingScreen;
