// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore } from "firebase/firestore";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBtxE-b7GHhLleHsSvXg6xp3Oj0dIzEomk",
  authDomain: "task-app-f01b2.firebaseapp.com",
  projectId: "task-app-f01b2",
  storageBucket: "task-app-f01b2.appspot.com",
  messagingSenderId: "701538688224",
  appId: "1:701538688224:web:2f7d7e3c923a23a5c2c485"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
export const db= getFirestore(app);