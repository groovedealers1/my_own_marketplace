import * as React from "react";
import {BrowserRouter, Route, Routes} from "react-router-dom";

import "./index.css";
import HomePage from "./components/HomePage.jsx";
import Card from "./components/Card.jsx";


function App(){
    return (
        <React.StrictMode>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<HomePage/>}/>
                    <Route path="/wear/:id" element={<Card/>}/>
                </Routes>
            </BrowserRouter>
        </React.StrictMode>
    );
}

export default App;