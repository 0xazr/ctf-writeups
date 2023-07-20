import { io } from "socket.io-client";

const socket = io("ws://amt.rs:31458/");

socket.on("systemMessage", (msg) => {
    console.log(`System: ${msg}`);
    if (msg.startsWith("amateursCTF")){
        console.log("Flag: " + msg);
        process.exit(0);
    }
});

socket.on("gameState", (state) => {
    // bruteforce
    if (state.phase === "question-answering") {
        for (let answer of state.phaseState.answers) {
            socket.emit("answerQuestion", answer);
        }
    }
});

socket.on("personalUpdate", (state) => {
    console.log(`Points: ${state.points}, Streak: ${state.streak}`);
});


