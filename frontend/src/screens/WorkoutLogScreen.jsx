// WorkoutLogScreen.js
import React, { useState } from "react";
import { View, Text, TextInput, Button, StyleSheet } from "react-native";

const WorkoutLogScreen = () => {
  const [activityType, setActivityType] = useState("");
  const [duration, setDuration] = useState("");

  const handleLogWorkout = () => {
    // Logic to save workout activity log
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Log Workout Activity</Text>
      <TextInput
        style={styles.input}
        placeholder="Activity Type"
        value={activityType}
        onChangeText={setActivityType}
      />
      <TextInput
        style={styles.input}
        placeholder="Duration (minutes)"
        value={duration}
        onChangeText={setDuration}
        keyboardType="numeric"
      />
      <Button title="Log Workout" onPress={handleLogWorkout} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
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

export default WorkoutLogScreen;