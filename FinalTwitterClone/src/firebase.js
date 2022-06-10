import firebase from "firebase";

const firebaseConfig = {
    apiKey: "AIzaSyB4-gzM77KNd1M8BoriU-Zn6ixk9eisCwE",
    authDomain: "messing-app-lm.firebaseapp.com",
    databaseURL: "https://messing-app-lm-default-rtdb.firebaseio.com",
    projectId: "messing-app-lm",
    storageBucket: "messing-app-lm.appspot.com",
    messagingSenderId: "740072413249",
    appId: "1:740072413249:web:0289e370ab0bff11e88ec0"
};

const firebaseApp = firebase.initializeApp(firebaseConfig);

const db = firebaseApp.firestore();

export default db;