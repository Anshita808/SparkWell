import React, { useState, useEffect } from "react";
import { StyleSheet, Text, View, Animated, Image } from "react-native";

const Splash = () => {
  const [isAnimationComplete, setAnimationComplete] = useState(false);
  const translateY = new Animated.Value(300);

  useEffect(() => {
    Animated.timing(translateY, {
      toValue: 0,
      duration: 1000, // Animation duration in milliseconds
      useNativeDriver: true,
    }).start(() => {
      setAnimationComplete(true);
    });
  }, []);

  return (
    <View style={styles.container}>
      <Animated.View
        style={[styles.animatedContainer, { transform: [{ translateY }] }]}
      >
        {isAnimationComplete && (
          <>
            <Image
              source={require("../image/yoga2.jpg")}
              style={styles.image}
            />
            <Text style={styles.text}>SPARKWELL</Text>
          </>
        )}
      </Animated.View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#ffffff",
  },
  animatedContainer: {
    justifyContent: "center",
    alignItems: "center",
  },
  image: {
    width: 150,
    height: 150,
    marginBottom: 20,
  },
  text: {
    color: "#00695C",
    fontSize: 40,
    fontWeight: "700",
  },
});

export default Splash;