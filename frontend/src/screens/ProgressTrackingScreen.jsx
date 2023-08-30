import React, { useState } from "react";
import { View, Text, StyleSheet } from "react-native";
import { Card, ProgressBar } from "react-native-paper";

const ProgressTrackingScreen = () => {
  const [completedGoals, setCompletedGoals] = useState(2); // Example: Replace with actual completed goals count
  const [totalGoals, setTotalGoals] = useState(5); // Example: Replace with actual total goals count

  const calculateProgressPercentage = () => {
    return (completedGoals / totalGoals) * 100;
  };

  return (
    <View style={styles.container}>
      <Card style={styles.card}>
        <Card.Content>
          <Text style={styles.title}>Progress Tracking</Text>
          <Text style={styles.text}>Total Goals: {totalGoals}</Text>
          <Text style={styles.text}>Completed Goals: {completedGoals}</Text>
          <ProgressBar
            progress={calculateProgressPercentage() / 100}
            color={"#EF5350"}
            style={{ height: 10, marginTop: 5 }} // Adjust the margin-top as needed
          />
          <Text style={{marginTop:5}} >
            Progress: {calculateProgressPercentage().toFixed(2)}%
          </Text>
        </Card.Content>
      </Card>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  card: {
    width: "80%", // Adjust the width as needed
    padding: 16,
    elevation: 4,
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 20,
  },
});

export default ProgressTrackingScreen;