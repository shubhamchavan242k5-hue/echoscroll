from django.shortcuts import render
import requests
from django.http import JsonResponse

def get_music_feed(request):
    query = request.GET.get('q', 'bollywood trending')
    url = f"https://itunes.apple.com/search?term={query}&entity=song&limit=50"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        results = data.get('results', [])
        
        music_data = []
        for track in results:
            music_data.append({
                'id': track.get('trackId'),
                'title': track.get('trackName'),
                'artist': track.get('artistName'),
                'audio_url': track.get('previewUrl'),
                'cover': track.get('artworkUrl100', '').replace('100x100bb', '800x800bb'), # High Quality
            })
        return JsonResponse(music_data, safe=False)
    except Exception as e:
        return JsonResponse([], safe=False)

def home(request):
    return render(request, 'index.html')