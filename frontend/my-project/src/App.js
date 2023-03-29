import List_page from "./pages/List_page";
import Detail_page from "./pages/detail_page";
import {Routes,Route,Router} from "react-router-dom"
import Notfound from "./pages/Notfound";
import React from "react";
import Login from "./pages/login";
import { RequireAuth } from "react-auth-kit";
import { UserContext } from "./UserContext";
import { useState } from "react";
// const LazyList = React.lazy(()=>import("./pages/List_page"))
function App() {
  const [value, setValue] = useState({token:null});

 





  return (
    <UserContext.Provider value={{value,setValue}}>
    <Routes>
      <Route path="/" element={
      <List_page />
      } />
      <Route path="/anime/:id" element={<RequireAuth loginPath="/login"><Detail_page /> </RequireAuth> } />
      <Route path="*" element={<Notfound />} />
      <Route path="/login" element={<Login />} />
      
    </Routes>
    </UserContext.Provider>
  );
  }

export default App;
