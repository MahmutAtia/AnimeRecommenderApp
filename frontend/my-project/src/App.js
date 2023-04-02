import List_page from "./pages/List_page";
import Detail_page from "./pages/detail_page";
import {Routes,Route,Router} from "react-router-dom"
import Notfound from "./pages/Notfound";
import React from "react";
import Login from "./pages/login";
import { RequireAuth } from "react-auth-kit";
import { UserContext } from "./UserContext";
import { useState } from "react";
import axios from "axios";
const LazyList = React.lazy(()=>import("./pages/List_page"))
function App() {
 


 
// set headers in axios
const setToken= function(token){
    if(token){
        axios.defaults.headers.common["Authorization"] = `Token ${token}`
    }
    else{
        delete axios.defaults.headers.common["Authorization"]
    }
}

// get token
const token = localStorage.getItem("token")
 





  return (
    <UserContext.Provider value={{token:token, setToken:setToken}}>
    <Routes>
      <Route path="/" element={
     token ? <LazyList /> : <Login />
      } />
      <Route path="/anime/:id" element={<RequireAuth loginPath="/login"><Detail_page /> </RequireAuth> } />
      <Route path="*" element={<Notfound />} />
      <Route  path="/login" element={ <Login />} />
      
    </Routes>
    </UserContext.Provider>
  );
  }

export default App;
