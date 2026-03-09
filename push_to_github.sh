#!/bin/bash
# JAZZY JELLYFISH - GitHub Push Script (Run from sda3 chroot)

set -e

REPO_DIR="/tmp/jazzy-ai-models"
REPO_NAME="jazzy-ai-models"

echo "🐙 JAZZY JELLYFISH - GitHub Repository Push"
echo "============================================"
echo ""

# Check if gh is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) not found!"
    echo ""
    echo "Install it first:"
    echo "  # On Ubuntu/Debian:"
    echo "  sudo apt install gh"
    echo ""
    echo "  # On Arch Linux:"
    echo "  sudo pacman -S github-cli"
    echo ""
    echo "Then authenticate:"
    echo "  gh auth login"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo "🔐 Not authenticated with GitHub. Running auth..."
    gh auth login
fi

cd "$REPO_DIR"

echo "📤 Creating GitHub repository..."
gh repo create "$REPO_NAME" \
    --public \
    --source=. \
    --description="Deep research database of 1000+ AI models from HuggingFace - Hidden gems, neuromorphic, reasoning, and multimodal models" \
    --push

echo ""
echo "✅ Repository created and pushed!"
echo ""
echo "🌐 View at: https://github.com/$(gh api user -q .login)/$REPO_NAME"
echo ""
echo "📊 Repository contains:"
echo "  - README.md (research report)"
echo "  - models_database.json (1006 models)"
echo "  - research_spider.py (research tool)"
echo "  - DEPLOYMENT_GUIDE.md (Jazzy Jellyfish setup)"
echo ""
echo "🎯 Next steps:"
echo "  1. Add topics: gh repo edit --add-topic ai,machine-learning,huggingface,llm,research"
echo "  2. Enable discussions: gh repo edit --enable-discussions"
echo "  3. Add README badge: gh repo edit --homepage https://jazzyjellyfish.ai"
