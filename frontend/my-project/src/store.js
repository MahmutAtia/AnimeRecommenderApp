import {configureStore} from "@reduxjs/toolkit"
import urlReducer, {search,addmamo} from "./features/urlSlice"
const store = configureStore(
{
    reducer:{
        url : urlReducer
    }
}
)

export default store