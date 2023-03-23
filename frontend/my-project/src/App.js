import List_page from "./pages/List_page";
import Detail_page from "./pages/detail_page";
import {Routes,Route} from "react-router-dom"
function App() {





  return (
    <Routes>
      <Route path="/" element={<List_page />} />
      <Route path="/anime/:id" element={<Detail_page />} />

    </Routes>
  );
  }

export default App;
