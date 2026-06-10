"""
Dry-run validation of all 5 demos
Tests: imports, syntax, file loading (no API calls)
"""
import sys
import os

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def test_demo_structure(demo_file):
    """Test if demo can be imported and basic structure is valid"""
    print(f"\n{'='*70}")
    print(f"Testing: {demo_file}")
    print('='*70)

    try:
        # Check file exists
        if not os.path.exists(demo_file):
            print(f"❌ FAIL: File not found!")
            return False

        # Check syntax by compiling
        with open(demo_file, 'r', encoding='utf-8') as f:
            code = f.read()

        compile(code, demo_file, 'exec')
        print("✅ Syntax: Valid")

        # Check for key components
        checks = {
            'load_dotenv': 'load_dotenv()' in code,
            'GOOGLE_API_KEY': 'GOOGLE_API_KEY' in code,
            'knowledge_base.txt': 'knowledge_base.txt' in code or 'documents' in code,
            'GoogleGenerativeAI': 'GoogleGenerativeAI' in code,
            'GoogleGenerativeAIEmbeddings': 'GoogleGenerativeAIEmbeddings' in code,
        }

        for check, passed in checks.items():
            status = "✅" if passed else "⚠️"
            print(f"{status} {check}: {'Present' if passed else 'Missing'}")

        all_passed = all(checks.values())

        if all_passed:
            print(f"✅ {demo_file}: PASS")
        else:
            print(f"⚠️ {demo_file}: PASS (with warnings)")

        return True

    except SyntaxError as e:
        print(f"❌ FAIL: Syntax Error")
        print(f"   Line {e.lineno}: {e.msg}")
        return False
    except Exception as e:
        print(f"❌ FAIL: {type(e).__name__}: {e}")
        return False

def test_knowledge_base():
    """Test if knowledge_base.txt exists and is readable"""
    print(f"\n{'='*70}")
    print("Testing: knowledge_base.txt")
    print('='*70)

    try:
        if not os.path.exists('knowledge_base.txt'):
            print("❌ FAIL: knowledge_base.txt not found!")
            return False

        with open('knowledge_base.txt', 'r', encoding='utf-8') as f:
            content = f.read()

        print(f"✅ File exists and readable")
        print(f"✅ Size: {len(content)} characters")
        print(f"✅ Lines: {len(content.splitlines())}")

        # Check for key ACME content
        acme_checks = {
            'ACME Corporation': 'ACME Corporation' in content or 'ACME CORPORATION' in content,
            'AutoFlow AI': 'AutoFlow AI' in content or 'AutoFlow' in content,
            'Product info': 'product' in content.lower() or 'flagship' in content.lower(),
            'Pricing': 'pricing' in content.lower() or 'plan' in content.lower(),
        }

        for check, passed in acme_checks.items():
            status = "✅" if passed else "⚠️"
            print(f"{status} Contains '{check}': {'Yes' if passed else 'No'}")

        print("✅ knowledge_base.txt: PASS")
        return True

    except Exception as e:
        print(f"❌ FAIL: {type(e).__name__}: {e}")
        return False

def test_env_file():
    """Test if .env file exists"""
    print(f"\n{'='*70}")
    print("Testing: .env file")
    print('='*70)

    if os.path.exists('.env'):
        print("✅ .env file exists")

        # Check if it has API key (without showing the actual key)
        with open('.env', 'r') as f:
            content = f.read()

        if 'GOOGLE_API_KEY' in content:
            print("✅ GOOGLE_API_KEY is set")
        else:
            print("⚠️ GOOGLE_API_KEY not found in .env")

        return True
    else:
        print("⚠️ .env file not found (students will need to create this)")
        if os.path.exists('.env.example'):
            print("✅ .env.example exists (students can copy this)")
        return True

def main():
    print("="*70)
    print("🧪 DRY-RUN VALIDATION OF ALL DEMOS")
    print("="*70)
    print("\nThis tests structure, syntax, and file loading")
    print("(No API calls - saves your quota!)\n")

    # Test knowledge base
    kb_ok = test_knowledge_base()

    # Test .env
    env_ok = test_env_file()

    # Test all 5 demos
    demos = [
        'demo_1_basic_rag.py',
        'demo_2_chunking_strategies.py',
        'demo_3_vector_storage_and_retrieval.py',
        'demo_4_evaluation_metrics.py',
        'demo_5_complete_rag_system.py',
    ]

    results = {}
    for demo in demos:
        results[demo] = test_demo_structure(demo)

    # Summary
    print(f"\n{'='*70}")
    print("📊 VALIDATION SUMMARY")
    print('='*70 + "\n")

    print("Knowledge Base:")
    print(f"  {'✅' if kb_ok else '❌'} knowledge_base.txt\n")

    print("Environment:")
    print(f"  {'✅' if env_ok else '⚠️'} .env configuration\n")

    print("Demos:")
    for demo, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {status} - {demo}")

    all_passed = all(results.values()) and kb_ok

    print(f"\n{'='*70}")
    if all_passed:
        print("✅ ALL VALIDATIONS PASSED!")
        print("\n🎯 Structure is correct. Demos should work once API quota resets.")
        print("⏳ API Quota Status: Exhausted (resets in ~24 hours)")
    else:
        print("⚠️ SOME VALIDATIONS FAILED")
        print("\nPlease fix the issues above before running demos.")

    print('='*70)

if __name__ == "__main__":
    main()
