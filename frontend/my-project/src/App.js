import List_page from "./pages/List_page";
import Detail_page from "./pages/detail_page";
import {Routes,Route} from "react-router-dom"
import Notfound from "./pages/Notfound";
import React from "react";
import Login from "./pages/login";
import { RequireAuth } from "react-auth-kit";

// const LazyList = React.lazy(()=>import("./pages/List_page"))
function App() {

  





  return (
    <Routes>
      <Route path="/" element={
      <List_page />
      } />
      <Route path="/anime/:id" element={<RequireAuth loginPath="/login"><Detail_page /> </RequireAuth> } />
      <Route path="*" element={<Notfound />} />
      <Route path="/login" element={<Login />} />

    </Routes>
  );
  }

export default App;
