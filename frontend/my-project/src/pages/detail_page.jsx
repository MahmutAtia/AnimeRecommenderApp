import { useParams } from 'react-router-dom'

import React from 'react'
import { useLocation } from 'react-router-dom'

export default function Detail_page() {
const location = useLocation()
 
  return (
    <div>{location.state}</div>
  )
}
