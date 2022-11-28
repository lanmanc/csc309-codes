import React from 'react';
import './App.css';
import Converter from "./components/Converter";
import Calculator from "./components/Calculator";
import Players from "./components/Players";
import APIContext, {useAPIContext} from "./Contexts/APIContext";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Layout from "./components/Layout";

function App() {
  const players = (
      <APIContext.Provider value={useAPIContext()}>
          <Players />
      </APIContext.Provider>
  )

  return (
    <BrowserRouter>
        <Routes>
            <Route path="/" element={<Layout />}>
                <Route index element={<Calculator />} />
                <Route path="calculator" element={<Calculator />} />
                <Route path="converter" element={<Converter />} />
                <Route path="players" element={players} />
            </Route>
        </Routes>
    </BrowserRouter>
  )
}

export default App;
