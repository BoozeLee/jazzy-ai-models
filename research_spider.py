#!/usr/bin/env python3
"""
JAZZY JELLYFISH - HUGGINGFACE DEEP RESEARCH SPIDER
Find hidden gems, exclusive models, and cutting-edge AI
"""

import requests
import json
from datetime import datetime
from collections import defaultdict

class HuggingFaceDeepResearch:
    def __init__(self):
        self.api_base = "https://huggingface.co/api"
        self.discoveries = {
            'hidden_gems': [],
            'neuromorphic': [],
            'reasoning': [],
            'code_specialists': [],
            'multimodal': [],
            'tiny_powerhouses': [],
            'experimental': [],
            'alien_tech': []  # 👽
        }
    
    def search_models(self, query, limit=100):
        """Search HuggingFace models"""
        url = f"{self.api_base}/models"
        params = {
            'search': query,
            'limit': limit,
            'sort': 'downloads',
            'direction': -1
        }
        try:
            response = requests.get(url, params=params, timeout=10)
            return response.json() if response.status_code == 200 else []
        except:
            return []
    
    def get_model_details(self, model_id):
        """Get detailed model info"""
        url = f"{self.api_base}/models/{model_id}"
        try:
            response = requests.get(url, timeout=10)
            return response.json() if response.status_code == 200 else {}
        except:
            return {}
    
    def analyze_model(self, model):
        """Deep analysis of model capabilities"""
        model_id = model.get('id', '')
        tags = model.get('tags', [])
        downloads = model.get('downloads', 0)
        likes = model.get('likes', 0)
        
        # Calculate "hidden gem" score
        # High quality but low popularity = hidden gem
        gem_score = likes / max(downloads, 1) * 1000000
        
        analysis = {
            'id': model_id,
            'downloads': downloads,
            'likes': likes,
            'gem_score': gem_score,
            'tags': tags,
            'size': self._estimate_size(model),
            'special_features': []
        }
        
        # Detect special capabilities
        model_lower = model_id.lower()
        tags_lower = ' '.join(tags).lower()
        
        if any(x in model_lower or x in tags_lower for x in ['snn', 'spike', 'neuromorphic', 'brain']):
            analysis['special_features'].append('NEUROMORPHIC')
            
        if any(x in model_lower or x in tags_lower for x in ['reason', 'cot', 'chain-of-thought', 'o1']):
            analysis['special_features'].append('REASONING')
            
        if any(x in model_lower or x in tags_lower for x in ['vision', 'multimodal', 'vlm', 'image']):
            analysis['special_features'].append('MULTIMODAL')
            
        if any(x in model_lower or x in tags_lower for x in ['1b', '2b', '3b']) and 'instruct' in tags_lower:
            analysis['special_features'].append('TINY_POWERHOUSE')
            
        if any(x in model_lower or x in tags_lower for x in ['experimental', 'research', 'alpha', 'beta']):
            analysis['special_features'].append('EXPERIMENTAL')
            
        if downloads < 1000 and likes > 50:
            analysis['special_features'].append('HIDDEN_GEM')
            
        return analysis
    
    def _estimate_size(self, model):
        """Estimate model size from name/tags"""
        model_str = str(model).lower()
        
        if '70b' in model_str or '72b' in model_str:
            return '40GB+'
        elif '34b' in model_str:
            return '20GB'
        elif '13b' in model_str or '14b' in model_str:
            return '8GB'
        elif '7b' in model_str or '8b' in model_str:
            return '4GB'
        elif '3b' in model_str:
            return '2GB'
        elif '1b' in model_str or '2b' in model_str:
            return '1GB'
        else:
            return 'Unknown'
    
    def deep_search(self):
        """Execute deep search across multiple categories"""
        
        print("🕷️  JAZZY JELLYFISH DEEP RESEARCH SPIDER")
        print("=" * 60)
        print("Searching HuggingFace for hidden gems...")
        print("")
        
        search_queries = [
            # Neuromorphic & Brain-inspired
            ('neuromorphic', 'neuromorphic'),
            ('spiking neural', 'neuromorphic'),
            ('brain-inspired', 'neuromorphic'),
            
            # Advanced reasoning
            ('reasoning', 'reasoning'),
            ('chain-of-thought', 'reasoning'),
            ('o1', 'reasoning'),
            ('monte carlo', 'reasoning'),
            
            # Code specialists
            ('code', 'code_specialists'),
            ('programming', 'code_specialists'),
            ('deepseek-coder', 'code_specialists'),
            ('starcoder', 'code_specialists'),
            
            # Multimodal
            ('vision language', 'multimodal'),
            ('multimodal', 'multimodal'),
            ('vlm', 'multimodal'),
            
            # Tiny but powerful
            ('1b instruct', 'tiny_powerhouses'),
            ('2b instruct', 'tiny_powerhouses'),
            ('3b instruct', 'tiny_powerhouses'),
            
            # Experimental/Research
            ('experimental', 'experimental'),
            ('research', 'experimental'),
            ('alpha', 'experimental'),
            
            # Specific cutting-edge
            ('qwen', 'code_specialists'),
            ('phi-3', 'tiny_powerhouses'),
            ('gemma', 'tiny_powerhouses'),
            ('mistral', 'reasoning'),
        ]
        
        all_models = {}
        
        for query, category in search_queries:
            print(f"🔍 Searching: {query}")
            models = self.search_models(query, limit=50)
            
            for model in models:
                model_id = model.get('id', '')
                if model_id and model_id not in all_models:
                    all_models[model_id] = model
        
        print(f"\n✓ Found {len(all_models)} unique models")
        print("🧠 Analyzing models...")
        print("")
        
        # Analyze all models
        analyzed = []
        for model_id, model in all_models.items():
            analysis = self.analyze_model(model)
            if analysis['special_features']:
                analyzed.append(analysis)
        
        # Sort by gem score
        analyzed.sort(key=lambda x: x['gem_score'], reverse=True)
        
        # Categorize
        for analysis in analyzed:
            for feature in analysis['special_features']:
                if feature == 'NEUROMORPHIC':
                    self.discoveries['neuromorphic'].append(analysis)
                elif feature == 'REASONING':
                    self.discoveries['reasoning'].append(analysis)
                elif feature == 'MULTIMODAL':
                    self.discoveries['multimodal'].append(analysis)
                elif feature == 'TINY_POWERHOUSE':
                    self.discoveries['tiny_powerhouses'].append(analysis)
                elif feature == 'EXPERIMENTAL':
                    self.discoveries['experimental'].append(analysis)
                elif feature == 'HIDDEN_GEM':
                    self.discoveries['hidden_gems'].append(analysis)
        
        return self.discoveries
    
    def generate_report(self):
        """Generate comprehensive report"""
        
        report = []
        report.append("# 🐙 JAZZY JELLYFISH - HUGGINGFACE DEEP RESEARCH REPORT")
        report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        report.append("## 🎯 HIDDEN GEMS (High Quality, Low Popularity)")
        report.append("")
        
        for model in self.discoveries['hidden_gems'][:10]:
            report.append(f"### {model['id']}")
            report.append(f"- **Size:** {model['size']}")
            report.append(f"- **Downloads:** {model['downloads']:,}")
            report.append(f"- **Likes:** {model['likes']}")
            report.append(f"- **Gem Score:** {model['gem_score']:.2f}")
            report.append(f"- **Features:** {', '.join(model['special_features'])}")
            report.append("")
        
        report.append("## 🧠 NEUROMORPHIC & BRAIN-INSPIRED")
        report.append("")
        for model in self.discoveries['neuromorphic'][:5]:
            report.append(f"- **{model['id']}** ({model['size']}) - {model['downloads']:,} downloads")
        
        report.append("")
        report.append("## 🤔 ADVANCED REASONING MODELS")
        report.append("")
        for model in self.discoveries['reasoning'][:10]:
            report.append(f"- **{model['id']}** ({model['size']}) - {model['downloads']:,} downloads")
        
        report.append("")
        report.append("## 💻 CODE SPECIALISTS")
        report.append("")
        for model in self.discoveries['code_specialists'][:10]:
            report.append(f"- **{model['id']}** ({model['size']}) - {model['downloads']:,} downloads")
        
        report.append("")
        report.append("## 👁️ MULTIMODAL (Vision + Language)")
        report.append("")
        for model in self.discoveries['multimodal'][:10]:
            report.append(f"- **{model['id']}** ({model['size']}) - {model['downloads']:,} downloads")
        
        report.append("")
        report.append("## ⚡ TINY POWERHOUSES (1-3B)")
        report.append("")
        for model in self.discoveries['tiny_powerhouses'][:10]:
            report.append(f"- **{model['id']}** ({model['size']}) - {model['downloads']:,} downloads")
        
        report.append("")
        report.append("## 🔬 EXPERIMENTAL/RESEARCH")
        report.append("")
        for model in self.discoveries['experimental'][:10]:
            report.append(f"- **{model['id']}** ({model['size']}) - {model['downloads']:,} downloads")
        
        return '\n'.join(report)

if __name__ == '__main__':
    spider = HuggingFaceDeepResearch()
    discoveries = spider.deep_search()
    
    report = spider.generate_report()
    
    # Save report
    with open('/tmp/huggingface_research_report.md', 'w') as f:
        f.write(report)
    
    # Save raw data
    with open('/tmp/huggingface_discoveries.json', 'w') as f:
        json.dump(discoveries, f, indent=2)
    
    print("✅ Research complete!")
    print("")
    print("Reports saved:")
    print("  - /tmp/huggingface_research_report.md")
    print("  - /tmp/huggingface_discoveries.json")
    print("")
    print(report)
