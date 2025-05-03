import { useState, useEffect } from "react"
import { Card, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"

export default function Dashboard() {
  const [log, setLog] = useState("")
  const [alerts, setAlerts] = useState([])
  const [suggestion, setSuggestion] = useState("")

  useEffect(() => {
    const interval = setInterval(() => {
      fetch("/api/ai/log").then(res => res.text()).then(setLog)
      fetch("/api/ai/alerts").then(res => res.json()).then(setAlerts)
      fetch("/api/ai/suggestion").then(res => res.text()).then(setSuggestion)
    }, 3000)

    return () => clearInterval(interval)
  }, [])

  return (
    <div className="p-4 grid grid-cols-1 md:grid-cols-3 gap-4">
      <Card className="col-span-2">
        <CardContent>
          <h2 className="text-xl font-bold mb-2">Live Log Feed</h2>
          <Textarea value={log} readOnly className="h-96" />
        </CardContent>
      </Card>

      <Card>
        <CardContent>
          <h2 className="text-xl font-bold mb-2">⚠️ Alerts</h2>
          <ul className="space-y-2">
            {alerts.map((a, i) => (
              <li key={i} className="text-red-600 font-mono">{a}</li>
            ))}
          </ul>
        </CardContent>
      </Card>

      <Card className="col-span-3">
        <CardContent>
          <h2 className="text-xl font-bold mb-2">🧠 Suggested Action</h2>
          <Textarea value={suggestion} readOnly className="h-32 font-semibold" />
        </CardContent>
      </Card>
    </div>
  )
}
