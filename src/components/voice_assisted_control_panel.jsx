import { useEffect, useState } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"

export default function VoicePanel() {
  const [voiceStatus, setVoiceStatus] = useState("Idle")
  const [transcript, setTranscript] = useState("")

  useEffect(() => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
    if (!SpeechRecognition) return

    const recognition = new SpeechRecognition()
    recognition.continuous = false
    recognition.lang = "en-US"
    recognition.interimResults = false
    recognition.maxAlternatives = 1

    recognition.onstart = () => setVoiceStatus("Listening...")
    recognition.onend = () => setVoiceStatus("Idle")

    recognition.onresult = (event) => {
      const command = event.results[0][0].transcript
      setTranscript(command)
      handleVoiceCommand(command.toLowerCase())
    }

    document.getElementById("start-voice").addEventListener("click", () => recognition.start())
  }, [])

  const handleVoiceCommand = (command) => {
    if (command.includes("generate report")) {
      fetch("/api/trigger/report").then(() => alert("📥 Report command sent"))
    }
    if (command.includes("status")) {
      alert("System status: Active and Monitoring")
    }
    if (command.includes("speak")) {
      const msg = new SpeechSynthesisUtterance("1man army is operational")
      window.speechSynthesis.speak(msg)
    }
  }

  return (
    <div className="p-4 space-y-4">
      <Card>
        <CardContent>
          <h2 className="text-xl font-bold">🎙️ Voice Assistant Panel</h2>
          <p>Status: <strong>{voiceStatus}</strong></p>
          <p>Last Command: <em>{transcript}</em></p>
          <Button id="start-voice" className="mt-4">Start Listening</Button>
        </CardContent>
      </Card>
    </div>
  )
}
