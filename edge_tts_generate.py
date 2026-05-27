#!/usr/bin/env python3
"""Edge TTS voice generator using asyncio"""
import sys
import asyncio
import subprocess

async def main():
    if len(sys.argv) < 3:
        print("Usage: python3 edge_tts_generate.py <text> <output_file>")
        sys.exit(1)
    
    text = sys.argv[1]
    output = sys.argv[2]
    
    try:
        import edge_tts
    except ImportError:
        print("Installing edge-tts...")
        subprocess.run([sys.executable, "-m", "pip", "install", "edge-tts", "-q"], check=True)
        import edge_tts
    
    print(f"Generating voice for: {text}")
    
    try:
        communicate = edge_tts.Communicate(text, voice="zh-CN-XiaoxiaoNeural")
        await communicate.save(output)
        print(f"Success! Saved to {output}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())