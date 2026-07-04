from django.shortcuts import render
import requests
from django.http import JsonResponse

def get_music_feed(request):
    # फ्रंटएंड से 'q' (query) मांगना, अगर कुछ न मिले तो 'trending' सर्च करना
    query = request.GET.get('q', 'trending bollywood')
    
    # iTunes API में सर्च करना (Limit 50 कर दी है ताकि हज़ारों गानों में से टॉप 50 आएं)
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
                'cover': track.get('artworkUrl100', '').replace('100x100bb', '600x600bb'),
            })
        return JsonResponse(music_data, safe=False)
    except Exception as e:
        return JsonResponse([], safe=False)

def home(request):
    return render(request, 'index.html')